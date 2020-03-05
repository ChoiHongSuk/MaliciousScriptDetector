# Malicious Script Detection Web Service
Malicious Script Detection Web Service는 사용자가 특정 의심 URL에 대해 검사가 필요할 때 사용된다.

# Architecture
<div>
  <img src="https://user-images.githubusercontent.com/43469662/75999615-d63e2300-5f45-11ea-8ea0-af65b58334f6.png"></img>
</div>

# Progress
1. 의심 URL에 대해 testphp.html의 입력란에 입력하여 전송
2. 가상환경(VMware를 사용하여 구축한 Ubuntu)에서 testphp.php를 통해 시그니쳐 분석 프로그램(Detect.py) 실행
3. 시그니쳐 분석 프로그램(Detect.py)
> - URL 복원 및 시그니쳐 분석
<div>
  <img src="https://user-images.githubusercontent.com/43469662/76002058-603bbb00-5f49-11ea-8591-65e096886b7b.png"></img>
</div>
</br>
    - 스크립트 추출
<div>
  <img src="https://user-images.githubusercontent.com/43469662/76002117-76497b80-5f49-11ea-89e8-daa58b1a634e.png"></img>
</div>
</br>
> - 난독화 해제
<div>
  <img src="https://user-images.githubusercontent.com/43469662/76002212-9bd68500-5f49-11ea-8196-aa5971e359c6.png"></img>
</div>
</br>
> - 시그니쳐 분석
<div>
  <img src="https://user-images.githubusercontent.com/43469662/76002267-af81eb80-5f49-11ea-857b-5be87493efd9.png"></img>
</div>
</br>
4. 분석한 결과를 Result.html에 표시함으로써 사용자에게 전달
