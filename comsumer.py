from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
print(consumer.bootstrap_connected())
for message in consumer:
    print (message)