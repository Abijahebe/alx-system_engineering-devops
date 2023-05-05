#!/usr/bin/env ruby

import sys
import re

# Define regular expression patterns for the sender, receiver, and flags
sender_pattern = r"\[from:(.*?)\]"
receiver_pattern = r"\[to:(.*?)\]"
flags_pattern = r"\[flags:(.*?)\]"

# Loop through each line of input
for line in sys.stdin:
    # Extract sender, receiver, and flags using regular expressions
    sender_match = re.search(sender_pattern, line)
  receiver_match = re.search(receiver_pattern, line)
  flags_match = re.search(flags_pattern, line)

  # If all required fields were found, print in desired format
  if sender_match and receiver_match and flags_match:
      sender = sender_match.group(1)
    receiver = receiver_match.group(1)
    flags = flags_match.group(1)
    print(f"{sender},{receiver},{flags}")
