from boto3_scripts.create_s3 import create_s3_bucket
from boto3_scripts.create_sns import create_sns_topic
from boto3_scripts.create_sqs import create_sqs_queue
from boto3_scripts.configure_notifications import configure_bucket_notifications

def main():
    """Fluxo principal de criação de recursos na AWS."""
    print("Iniciando a criação dos recursos AWS...")

    # 1. Criar Bucket S3
    bucket_name = "bucket-jltdsjr"
    create_s3_bucket(bucket_name)

    # 2. Criar Tópico SNS
    topic_name = "MeuTopicoSNS"
    topic_arn = create_sns_topic(topic_name)

    # 3. Criar Fila SQS
    queue_name = "MinhaFilaSQS"
    create_sqs_queue(queue_name)

    # 4. Configurar Notificações do S3 para SNS
    configure_bucket_notifications(bucket_name, topic_arn)

    print("Recursos criados com sucesso!")

if __name__ == "__main__":
    main()
