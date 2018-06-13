instance_types:
	@./instance_types/main.py

cloudwatch_logs:
	@./cloudwatch_logs/main.py

.PHONY: instance_types cloudwatch_logs
