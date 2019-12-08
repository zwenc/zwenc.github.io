function copyUrl2() {
	if(/Android|webOS|iPhone|iPad|BlackBerry/i.test(navigator.userAgent)) {
		alert("移动端不支持点击复制");
		return;
	}

	var Url2 = document.getElementById("mymail").innerText;
	var oInput = document.createElement('input');
	oInput.style = "";
	oInput.value = Url2;
	document.body.appendChild(oInput);
	oInput.select(); // 选择对象
	document.execCommand("Copy"); // 执行浏览器复制命令
	alert('已成功复制到剪切板');
}