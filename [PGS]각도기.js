//나의 풀이
function solution(angle) {
  var answer = 0;
  if (angle === 90) answer = 2;
  else if (angle === 180) answer = 4;
  else if (angle > 0 && angle < 90) answer = 1;
  else if (angle > 90 && angle < 180) answer = 3;
  return answer;
}

//우수 정답
//1. filter
function solution(angle) {
  return [0, 90, 91, 180].filter((x) => angle >= x).length;
}

function solution(angle) {
  return angle < 90 ? 1 : angle === 90 ? 2 : angle < 180 ? 3 : 4;
}
