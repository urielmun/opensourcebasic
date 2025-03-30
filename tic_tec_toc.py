#####################
#프로그램명: tic_tec_toc.py
#학과: 소프트웨어학부 인공지능학과
#학번: 2022042011
#이름: 문서영
#작성일자: 2025.03.30(토)
#프로그램 설명: 틱택토 구현
#####################
import random

def choosePlayer():
    print('대문자 영문자 X 또는 O 입력하세요.')  # 문구 수정
    while True:
        chosen = input('입력: ').upper()  # 사용자 입력을 대문자로 처리
        if chosen != 'O' and chosen != 'X':
            print('영문자 O 또는 X를 다시 입력하세요.')
            continue
        elif chosen == 'O':  # AI가 선공
            return 'O', 'X'
        elif chosen == 'X':  # 플레이어가 선공
            return 'X', 'O'

def drawingBoard(screen):
    print()
    print('───────────────────────')
    print(' ' + screen[6] + ' │ ' + screen[7] + ' │ ' + screen[8])
    print('───────────────────────')
    print(' ' + screen[3] + ' │ ' + screen[4] + ' │ ' + screen[5])
    print('───────────────────────')
    print(' ' + screen[0] + ' │ ' + screen[1] + ' │ ' + screen[2])
    print('───────────────────────')
    print()

def putPlayerStone(screen, mark):
    while True:
        print('>> 돌 위치 선택: ', end='')
        position = input()
        if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue
        if screen[int(position)-1] != '':  # 이미 수가 놓여 있다면..
            continue
        else:
            break
    screen[int(position)-1] = mark  # player의 '수' 놓기
    return position, screen

def putAIStone(screen, player, AI):
    AI_willPut_here = []  # AI가 놓을 위치
    Put_player = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        if player == screen[i]:
            Put_player[i] = True
    Put_AI = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        if AI == screen[i]:
            Put_AI[i] = True

    # 가로, 세로, 대각선 체크 로직 추가 필요

    # '수' 놓을 자리 선택
    for i in range(0, 9):
        if screen[i] == '':
            AI_willPut_here.append(i)
    available = random.choice(AI_willPut_here)
    screen[available] = AI
    return screen

def checkWinner(screen, player, AI):
    playerPut = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        if player == screen[i]:
            playerPut[i] = True

    # 세로 확인
    for i in range(3):
        if playerPut[i] and playerPut[i+3] and playerPut[i+6]:
            playerWin(screen)
            return True

    # 가로 확인
    for i in range(0, 9, 3):
        if playerPut[i] and playerPut[i+1] and playerPut[i+2]:
            playerWin(screen)
            return True

    # 대각선 확인
    if playerPut[0] and playerPut[4] and playerPut[8]:
        playerWin(screen)
        return True
    if playerPut[2] and playerPut[4] and playerPut[6]:
        playerWin(screen)
        return True

    for i in range(0, 9):
        if screen[i] == '':
            break
    else:
        print('무승부')
        return True

    return False

def playerWin(screen):
    drawingBoard(screen)
    print('플레이어 승리!')

if __name__ == "__main__":
    while True:
        gameScreen = ['', '', '', '', '', '', '', '', '']  # 보드 순서 789 456 123
        player, AI = choosePlayer()  # 게임 순서 결정하기
        drawingBoard(gameScreen)  # 보드 그리기
        if player == 'X':  # 플레이어가 선공을 하는 경우
            while True:  # 사용자 플레이
                putPlayerStone(gameScreen, player)  # 먼저 수를 놓는다.
                if checkWinner(gameScreen, player, AI):  # 승패 결정
                    break
                drawingBoard(gameScreen)  # 보드 그리기
                putAIStone(gameScreen, player, AI)  # AI 플레이
                if checkWinner(gameScreen, player, AI):  # 승패 결정
                    break
                drawingBoard(gameScreen)  # 보드 그리기
        else:  # AI가 선공을 하는 경우
            while True:
                putAIStone(gameScreen, player, AI)  # AI가 먼저 수를 놓는다.
                if checkWinner(gameScreen, player, AI):  # 승패 결정
                    break
                drawingBoard(gameScreen)  # 보드 그리기
                putPlayerStone(gameScreen, player)  # 플레이어 수 놓기
                if checkWinner(gameScreen, player, AI):  # 승패 결정
                    break
                drawingBoard(gameScreen)  # 보드 그리기
