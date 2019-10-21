from rest_framework.views import APIView
from rest_framework.response import Response
from team.models.member import Member
from team.serializer.member import Member as MemberSerializer
from rest_framework.parsers import JSONParser
import json


class MemberService(APIView):

    def get(self, request):
        requested_uuid = request.GET.get('uuid')

        if requested_uuid:
            member = Member.objects.all().filter(uuid=requested_uuid)
            return Response(MemberSerializer(member, many=True).data)

        members = Member.objects.all()
        return Response(MemberSerializer(members, many=True).data)

    def post(self, request):
        serializer = MemberSerializer(data=json.loads(request.body))
        print serializer.initial_data
        serializer.is_valid()
        print serializer.validated_data
        member = serializer.save()
        created_member = Member.objects.all().filter(uuid=member.uuid)
        return Response(MemberSerializer(created_member, many=True).data)
