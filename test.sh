#!/bin/bash
notify_exit () {
  echo "exit child by SIGTERM"
  exit 1
}

trap "notify_exit" SIGTERM SIGINT
echo "child process"
sleep 20
