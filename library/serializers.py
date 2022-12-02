from rest_framework import serializers

class bookSerializer(serializer.Serializers):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    name=serializers.CharField(max_length=30)
    isbn=serializers.PositiveIntegerField()
    author=serializers.CharField(max_length=40)
    category=serializers.CharField(max_length=30,choices=catchoice,default='education')