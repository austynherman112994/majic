from pulsar import Client
import json

def publish_message(topic, message):
  """
  Publishes a message to the specified Apache Pulsar topic.

  Args:
    topic: The name of the Pulsar topic to publish to.
    message: The message to publish.
  """
  try:
    # Create a Pulsar client
    client = Client('pulsar://10.107.141.190:6650')

    # Create a producer for the specified topic
    producer = client.create_producer(topic)

    # Publish the message
    producer.send(message.encode('utf-8'))

    print(f"Message '{message}' published successfully to topic '{topic}'")

  except Exception as e:
    print(f"Error publishing message: {e}")

  finally:
    # Close the producer and client
    producer.close()
    client.close()

# Example usage
topic_name = "test-upstream-0001"
message_to_publish = json.dumps({
    'arg_1_nested': {
        'arg_1': 'a',
        'arg_2': [1,2,3,4,5,6]
    },
    'arg_2': 'rg_2',
    'kwarg_val_1': 'k1',
    'kwarg_val_2': 'k2'
})

publish_message(topic_name, message_to_publish)
