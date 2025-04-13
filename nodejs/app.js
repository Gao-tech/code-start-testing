const express = require("express");
const serverlessExpress = require("@vendia/serverless-express");

const app = express();

app.get("/node", (req, res) => {
  res.json({ message: "Start Serverless Node.js" });
});

// Create handler separately
const handler = serverlessExpress({ app });

exports.handler = async (event, context) => {
  return handler(event, context);
};
