#!/usr/bin/env bash
set -u

# Read-only student preflight for NRP/Nautilus.
# Usage:
#   bash national_research_platform/scripts/student_preflight.sh <course-namespace>
#
# This script intentionally does not create, delete, or modify Kubernetes resources.
# It also never prints kubeconfig contents or token values.

NAMESPACE="${1:-}"

if [[ -z "${NAMESPACE}" ]]; then
  echo "usage: $0 <course-namespace>" >&2
  echo "example: $0 swosu-jevert-cs2-f26" >&2
  exit 2
fi

failures=0

section() {
  printf '\n== %s ==\n' "$1"
}

check_cmd() {
  local cmd="$1"
  if command -v "$cmd" >/dev/null 2>&1; then
    printf '[OK] %s found: %s\n' "$cmd" "$(command -v "$cmd")"
    return 0
  fi

  printf '[FAIL] %s not found on PATH\n' "$cmd"
  failures=$((failures + 1))
  return 1
}

section "Local tools"
check_cmd kubectl || true
check_cmd kubectl-oidc_login || true

if ! command -v kubectl >/dev/null 2>&1; then
  printf '\nCannot continue Kubernetes checks until kubectl is installed.\n'
  exit 1
fi

section "kubectl version"
kubectl version --client 2>&1 || failures=$((failures + 1))

section "Available contexts"
kubectl config get-contexts 2>&1 || failures=$((failures + 1))

section "Current context"
current_context="$(kubectl config current-context 2>/dev/null || true)"
if [[ -n "${current_context}" ]]; then
  printf 'current context: %s\n' "${current_context}"
else
  printf '[FAIL] no current Kubernetes context\n'
  failures=$((failures + 1))
fi

section "Target namespace"
printf 'namespace under test: %s\n' "${NAMESPACE}"
printf 'This script uses -n explicitly; it does not change your default namespace.\n'

section "Read access"
if kubectl auth can-i get pods -n "${NAMESPACE}" 2>&1 | tee /tmp/nrp-preflight-can-get-pods.$$ | grep -qx 'yes'; then
  printf '[OK] identity may get pods in %s\n' "${NAMESPACE}"
else
  printf '[FAIL] identity may not get pods in %s\n' "${NAMESPACE}"
  failures=$((failures + 1))
fi
rm -f /tmp/nrp-preflight-can-get-pods.$$

section "Job permission"
if kubectl auth can-i create jobs -n "${NAMESPACE}" 2>&1 | tee /tmp/nrp-preflight-can-create-jobs.$$ | grep -qx 'yes'; then
  printf '[OK] identity may create jobs in %s\n' "${NAMESPACE}"
else
  printf '[FAIL] identity may not create jobs in %s\n' "${NAMESPACE}"
  failures=$((failures + 1))
fi
rm -f /tmp/nrp-preflight-can-create-jobs.$$

section "Namespace visibility"
if kubectl get pods -n "${NAMESPACE}" --request-timeout=20s 2>&1; then
  printf '[OK] namespace read completed\n'
else
  printf '[FAIL] namespace read failed\n'
  failures=$((failures + 1))
fi

section "Result"
if [[ "${failures}" -eq 0 ]]; then
  printf 'PREFLIGHT PASS: local tools, authentication, namespace read, and basic Job permission look ready.\n'
  printf 'No Kubernetes resources were created or deleted.\n'
  exit 0
fi

printf 'PREFLIGHT NEEDS ATTENTION: %d check(s) did not pass.\n' "${failures}"
printf 'Preserve the command/output that failed. Do not paste tokens or kubeconfig contents into a help request.\n'
printf 'If you were just added to the namespace, the NRP docs recommend: kubectl oidc-login clean\n'
exit 1
