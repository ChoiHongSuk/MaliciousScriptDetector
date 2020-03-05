# Malicious Script Detection Web Service
Malicious Script Detection Web Service는 사용자가 특정 의심 URL에 대해 검사가 필요할 때 사용된다.

# Usage Tech
Ubuntu, Apache TomCat, Python, JavaScript, PHP, MySQL

# Architecture
<div>
  <img src="https://user-images.githubusercontent.com/43469662/75999615-d63e2300-5f45-11ea-8ea0-af65b58334f6.png"></img>
</div>

# Progress
1. 의심 URL에 대해 testphp.html의 입력란에 입력하여 전송
2. 가상환경(VMware를 사용하여 구축한 Ubuntu)에서 testphp.php를 통해 시그니쳐 분석 프로그램(Detect.py) 실행
3. 시그니쳐 분석 프로그램(Detect.py)
> - URL 복원 및 시그니쳐 분석
> > <img src="https://user-images.githubusercontent.com/43469662/76003813-ec4ee200-5f4b-11ea-89c4-ce96b27a545f.png" weight="500" height="200"></img>
> - 스크립트 추출
> > <img src="https://user-images.githubusercontent.com/43469662/76003878-0a1c4700-5f4c-11ea-9b53-2709e4d2882d.png" weight="500" height="200"></img>
> - 난독화 해제
> > <img src="https://user-images.githubusercontent.com/43469662/76003907-11dbeb80-5f4c-11ea-85b4-9a9eba39df9e.png" weight="500" height="200"></img>
> - 시그니쳐 분석
> > <img src="https://user-images.githubusercontent.com/43469662/76003918-16080900-5f4c-11ea-97f1-05a489ed48b5.png" weight="500" height="200"></img>
4. 분석한 결과를 Result.html에 표시함으로써 사용자에게 전달
