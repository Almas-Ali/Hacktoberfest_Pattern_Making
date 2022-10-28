for ($i = 1; $i -le 5 * 2; $i+=2) {
    Write-Output "$(" "*([math]::Floor(5 - $i / 2)))$("*" * $i)"
}
for ($i = 0; $i -lt 5; $i++) {
    Write-Output "   ***"
}
