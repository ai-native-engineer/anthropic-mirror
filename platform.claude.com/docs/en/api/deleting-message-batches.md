<!-- source: https://platform.claude.com/docs/en/api/deleting-message-batches -->

# Delete a Message Batch
DELETE/v1/messages/batches/{message_batch_id}
Delete a Message Batch.
Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Path ParametersExpand Collapse 
message_batch_id: string
ID of the Message Batch.
[](https://platform.claude.com/docs/en/api/messages/batches/delete#delete.message_batch_id)
DeletedMessageBatch object { id, type } 
ID of the Message Batch.
[](https://platform.claude.com/docs/en/api/messages/batches/delete#deleted_message_batch.id)
type: "message_batch_deleted"
Deleted object type.
For Message Batches, this is always `"message_batch_deleted"`.
[](https://platform.claude.com/docs/en/api/messages/batches/delete#deleted_message_batch.type)
[](https://platform.claude.com/docs/en/api/messages/batches/delete#deleted_message_batch)
Delete a Message Batch
cURL

curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
    -X DELETE \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
