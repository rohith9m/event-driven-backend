resource "aws_dynamodb_table" "requests_table" {
  name         = "${var.project_name}-${var.environment}-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "request_id"

  attribute {
    name = "request_id"
    type = "S"
  }
}

resource "aws_sqs_queue" "request_queue" {
  name = "${var.project_name}-${var.environment}-queue"
}

resource "aws_sns_topic" "notifications" {
  name = "${var.project_name}-${var.environment}-notifications"
}

