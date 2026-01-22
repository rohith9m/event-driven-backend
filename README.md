# Event-Driven Serverless Backend (AWS)

This project demonstrates the design of a scalable, event-driven serverless backend using AWS managed services and Infrastructure as Code principles. The architecture focuses on asynchronous processing, loose coupling, and cost-aware cloud design.

---

## Architecture Overview

The system follows an event-driven pattern where incoming requests are processed asynchronously to improve scalability and reliability.

**Flow:**
Producer → Amazon SQS → AWS Lambda → Amazon DynamoDB  
                  └→ Amazon SNS (notifications)

---

## Core Components

- **Amazon SQS**  
  Acts as a message queue to decouple producers from consumers and handle traffic spikes reliably.

- **AWS Lambda**  
  Processes messages from SQS, performs business logic, and orchestrates downstream actions.

- **Amazon DynamoDB**  
  Serverless NoSQL database used to persist processed request data with on-demand scaling.

- **Amazon SNS**  
  Sends notifications after successful processing of requests.

- **IAM (Least Privilege)**  
  Custom IAM roles and policies restrict Lambda access to only required AWS resources.

---

## Infrastructure as Code

All cloud resources are provisioned using **Terraform**, enabling:
- Repeatable and version-controlled infrastructure
- Environment consistency
- Easy teardown and recreation of resources

---

## Design Considerations

- **Event-driven architecture** to improve scalability and fault tolerance  
- **Asynchronous processing** using SQS to avoid tight coupling  
- **Serverless services** to minimize operational overhead  
- **Cost-aware design** using pay-per-use AWS services  
- **Security-first approach** with least-privilege IAM policies  

