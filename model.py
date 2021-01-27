import pika
import pickle
import numpy as np
with open('myfile.pkl', 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)
#connect to server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Features')

#Напишем функцию, определяющую, как работать с полученным сообщением:
def callback(ch, method, properties, body):
    print(f'Получен вектор признаков {body}')

#Зададим правила чтения из очереди, указанной в параметре queue:
# on_message_callback показывает какую функцию вызвать при получении сообщения
channel.basic_consume(
    queue='Features', on_message_callback=callback, auto_ack=True)
print('...Ожидание сообщений, для выхода нажмите CTRL+C')

channel.start_consuming()