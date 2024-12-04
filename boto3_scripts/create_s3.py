import boto3

def create_s3_bucket(bucket_name='bucket-jltdsjr', region='us-east-1'):
    """Cria um bucket no Amazon S3 na região especificada."""
    s3_client = boto3.client('s3', region_name=region)

    try:
        # Configuração necessária para buckets em regiões específicas
        response = s3_client.create_bucket(
            Bucket=bucket_name
            
        )
        print(f"Bucket '{bucket_name}' criado com sucesso na região {region}.")
    except Exception as e:
        print(f"Erro ao criar bucket: {e}")

# Exemplo de uso
create_s3_bucket('bucket-jltdsjr')
