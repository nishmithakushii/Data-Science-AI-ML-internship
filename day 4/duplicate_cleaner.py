raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

print("ID05" in unique_users)

print("Original count:", len(raw_logs))
print("Unique count:", len(unique_users))

print("Unique User IDs:", unique_users)

