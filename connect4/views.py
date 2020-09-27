from django.shortcuts import render
from rest_framework.views import APIView
from .models import Game,Audit
from rest_framework.response import Response
from rest_framework import status
from .validator import check_validity,check_winner
from rest_framework import generics
from .serializers import AuditSerializer
# Create your views here.


class Start(APIView):

    def get(self, request, format=None):
        game=Game.objects.create()
        return Response({"game":game.id, "message": "READY"}, status=status.HTTP_201_CREATED )


class Play(APIView):

    def post(self, request, format=None):
        game_id=request.data.get("game_id")
        column=request.data.get("column")
        game=Game.objects.get(pk=game_id)
        respone={}

        if not game.active:
            respone["win"]= "Game over, " + check_winner(game.board)
        else:
            audit=Audit()
            audit.game=game_id
            audit.old_state=game.board
            move_validity=check_validity(game.turn,column,game.board)
            respone["move"]=move_validity
            winner=check_winner(game.board)
            if winner:
                respone["win"]=winner
                game.active=False
            game.turn=game.turn+1
            game.save()
            audit.new_state=game.board
            audit.save()
        return Response(respone)

class AuditView(APIView):
 
    def get(self, request, game):
        audits = Audit.objects.filter(game=game)
        data = AuditSerializer(audits, many=True).data
        return Response(data, status=status.HTTP_200_OK)


