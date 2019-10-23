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
            member = Member.objects.filter(uuid=requested_uuid).first()
            return Response(MemberSerializer(member).data)

        members = Member.objects.all()
        return Response(MemberSerializer(members, many=True).data)

    def post(self, request):
        serializer = MemberSerializer(data=json.loads(request.body))
        serializer.is_valid()
        member = serializer.save()
        return Response(MemberSerializer(member).data)

    def put(self, request):
        data = json.loads(request.body)
        uuid = data['uuid']
        existing_member = Member.objects.filter(uuid=uuid).first()
        serializer = MemberSerializer(existing_member, data=data)
        serializer.is_valid()
        member = serializer.save()
        return Response(MemberSerializer(member).data)

    def patch(self, request):
        data = json.loads(request.body)
        uuid = data['uuid']
        existing_member = Member.objects.filter(uuid=uuid).first()
        serializer = MemberSerializer(existing_member, data=data)
        serializer.is_valid()
        member = serializer.save()
        return Response(MemberSerializer(member).data)
