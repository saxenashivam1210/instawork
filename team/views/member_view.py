from rest_framework.views import APIView
from rest_framework.response import Response
from team.models.member import Member
from team.serializer.member import Member as MemberSerializer
import json


class MemberService(APIView):
    @staticmethod
    def get(request):
        requested_uuid = request.GET.get('uuid')

        if requested_uuid:
            member = Member.objects.filter(uuid=requested_uuid).first()
            if member:
                return Response(MemberSerializer(member).data)
            else:
                return Response(status=404, data={"message": "Record with uuid {} does not exist".format(requested_uuid)})

        members = Member.objects.all()
        return Response(MemberSerializer(members, many=True).data)

    @staticmethod
    def post(request):
        serializer = MemberSerializer(data=json.loads(request.body))
        serializer.is_valid()
        member = serializer.save()
        return Response(MemberSerializer(member).data)

    @staticmethod
    def put(request):
        data = json.loads(request.body)
        uuid = data['uuid']
        existing_member = Member.objects.filter(uuid=uuid).first()
        serializer = MemberSerializer(existing_member, data=data)
        serializer.is_valid()
        member = serializer.save()
        return Response(MemberSerializer(member).data)

    @staticmethod
    def delete(request):
        requested_uuid = request.GET.get('uuid')
        deleted = Member.objects.filter(uuid=requested_uuid).delete()
        if deleted and deleted[0] == 1:
            return Response(status=200, data={"message": "Record deleted"})
        else:
            return Response(status=404, data={"message": "Record with uuid {} does not exist".format(requested_uuid)})
