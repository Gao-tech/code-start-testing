// package main

// import (
// 	"context"
// 	"github.com/aws/aws-lambda-go/lambda"
// )

// func handler(ctx context.Context) (map[string]string, error) {
// 	return map[string]string{
// 		"message": "Start Serverless Go",
// 	}, nil
// }

// func main() {
// 	lambda.Start(handler)
// }


package main

import (
	"context"
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

func handler(ctx context.Context) (events.APIGatewayProxyResponse, error) {
	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Headers:    map[string]string{"Content-Type": "application/json"},
		Body:       `{"message": "Start Serverless Go"}`,
	}, nil
}

func main() {
	lambda.Start(handler)
}