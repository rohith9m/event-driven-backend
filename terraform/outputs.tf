output "dynamodb_table" {
  value = aws_dynamodb_table.requests_table.name
}

output "sqs_queue" {
  value = aws_sqs_queue.request_queue.name
}

output "sns_topic" {
  value = aws_sns_topic.notifications.name
}

