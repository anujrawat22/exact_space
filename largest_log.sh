largest_log_file=$(find / -type f -name "*.log" 2>/dev/null | xargs du -b | sort -n | tail -1 | cut -f2)

if [ -z "$largest_log_file" ]; then
    echo "No log file found"
    exit 1
fi

echo "Largest log file is: $largest_log_file"

tail -n 100 "$largest_log_file" > "${largest_log_file}.tmp" && mv "${largest_log_file}.tmp" "$largest_log_file"
