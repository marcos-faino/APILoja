from django.db.models import Avg
from rest_framework import serializers

from .models import Categoria, Produto, Avaliacao


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id',
            'descricao',
            'criacao',
            'atualizacao',
            'ativo',
        )


class ProdutoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    avaliacoes = 'AvaliacaoSerializer(many=True, read_only=True)'

    media_avaliacoes = serializers.SerializerMethodField();

    # HyperLinked Related Field
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = (
            'id',
            'nome',
            'preco',
            'categoria',
            'criacao',
            'atualizacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )

    def get_media_avaliacoes(self, produto):
        media = produto.avaliacoes.aggregate(Avg('nota')).get('nota__avg')

        if media is None:
            return 0
        return round(media)


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'produto',
            'avaliador',
            'email',
            'comentario',
            'nota',
            'criacao',
            'atualizacao',
            'ativo',
        )

    def validate_nota(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação deve ser de 1 a 5 pontos')