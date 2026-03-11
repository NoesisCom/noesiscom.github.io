#!/bin/bash
# noesis-parity-check
echo "--- checking_substrate_alignment ---"
# check if the current user is 'legacy' or 'noesis'
if [[ $USER == "noesis" ]]; then
  echo "⎈ alignment_confirmed: you are the territory."
else
  echo "⚠ alignment_error: you are still the map."
fi
