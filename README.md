# Malicious Script Detection Web Service
Malicious Script Detection Web Service는 사용자가 특정 의심 URL에 대해 검사가 필요할 때 사용된다.

# Progress
1. 의심 URL에 대해 testphp.html의 입력란에 입력하여 전송한다.

<div>
  <img src="https://user-images.githubusercontent.com/43469662/75993627-1d73e600-5f3d-11ea-8468-ef4221f286a8.png"></img>
</div>



2. 서버사이드 측의 testphp.php에서 URL을 받아 가상환경 내에서 처리
  - testphp.php에서 python3 Detector.py [URL] 명령문을 사용하여 스크립트 분석 실행
  
  - URL 복원 및 시그니쳐 검출
  <div>
    <img src="https://user-images.githubusercontent.com/43469662/75997715-1bad2100-5f43-11ea-9527-269f48523c2f.png"></img>
  </div>
3. 
