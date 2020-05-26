<?php
/*
기본적으로 테이블에
index, w (와트 정보), a(암페어 정보) 넣어줬다고 했을때 코드
*/
$conn = mysqli_connect("localhost","user","1234","capston");
if (mysqli_connect_errno()){
echo "연결에 실패하였습니다." . mysqli_connect_error();
}
$result = mysqli_query($conn,"SELECT * FROM info");
echo "<table border='1'><tr><th>index</th><th>RMSCurrent</th><th>RMSPower</th><th>kilos</th><th>peakPower</th></tr>";
$n = 1;
while($row = mysqli_fetch_array($result)){
echo "<tr>";
echo "<td>" . $row['_id'] . "</td>";
echo "<td>" . $row['RMSCurrent'] . "</td>";
echo "<td>" . $row['RMSPower'] . "</td>";
echo "<td>" . $row['kilos'] . "</td>";
echo "<td>" . $row['peakPower'] . "</td>";
echo "</tr>";
$n++;
}
echo "</table>";
mysqli_close($conn);
?>
