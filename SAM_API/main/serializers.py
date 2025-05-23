from .models import TeacherUsersStats, TeacherTopic
from rest_framework import serializers
from django.core.validators import MinValueValidator

__all__ = [
    'TeacherUsersStatsSerializer',
    'TeacherEditSerializer',
    'TopicsSerializer',
    'TopicedTeachersSerializer',
    'TeacherTopicSerializer'
]


class TeacherTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTopic
        fields = ['topic_name']


class TeacherUsersStatsSerializer(serializers.ModelSerializer):
    topic_name = TeacherTopicSerializer(source='topic', many=True, read_only=True)
    
    class Meta:
        model = TeacherUsersStats
        fields = [
            'juda_ham_qoniqaman', 
            'ortacha_qoniqaman', 
            'asosan_qoniqaman', 
            'qoniqmayman', 
            'umuman_qoniqaman', 
            'updated_at', 
            'topic_name'
        ]


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTopic
        fields = ['topic_name']

class TopicedTeachersSerializer(serializers.ModelSerializer):
    topics = TeacherTopicSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherUsersStats
        fields = ["id", "full_name", "topics", "telegram_id"]


from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import TeacherUsersStats 

class TeacherUsersStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherUsersStats
        fields = '__all__'


class TeacherEditSerializer(serializers.ModelSerializer):
    
    m1_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m1_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m1_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m1_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m1_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    m2_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m2_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m2_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m2_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m2_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    m3_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m3_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m3_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m3_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m3_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    m4_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m4_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m4_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m4_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m4_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    m5_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m5_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m5_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m5_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m5_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    m6_juda_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m6_yaxshi = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m6_ortacha = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m6_past = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])
    m6_yomon = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        model = TeacherUsersStats
        fields = [
            
            'm1_juda_yaxshi', 'm1_yaxshi', 'm1_ortacha', 'm1_past', 'm1_yomon',
            
            'm2_juda_yaxshi', 'm2_yaxshi', 'm2_ortacha', 'm2_past', 'm2_yomon',
            
            'm3_juda_yaxshi', 'm3_yaxshi', 'm3_ortacha', 'm3_past', 'm3_yomon',
            
            'm4_juda_yaxshi', 'm4_yaxshi', 'm4_ortacha', 'm4_past', 'm4_yomon',
            
            'm5_juda_yaxshi', 'm5_yaxshi', 'm5_ortacha', 'm5_past', 'm5_yomon',
            
            'm6_juda_yaxshi', 'm6_yaxshi', 'm6_ortacha', 'm6_past', 'm6_yomon',
        ]

    def validate(self, data):
        return data
