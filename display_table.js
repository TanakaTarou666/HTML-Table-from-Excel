// チェックするキーのリスト
const keysToCheck = ['Image'];

function generateTable(table_data) {
    // データからHTML表を生成
    let html = '<table border="1">';
    html += '<tr>';
    
    for (const key in table_data[0]) {
            html += '<th>' + key + '</th>';
    }
    html += '</tr>';
    for (let i = 0; i < table_data.length; i++) {
        const row = table_data[i];
        html += '<tr>';
        for (const key in row) {
            if(keysToCheck.includes(key)){
                html += '<td><img src="' + row[key] + '"  height="100"></td>'; 
            }else{
                html += '<td>' + row[key] + '</td>';
            }
        }
        html += '</tr>';
    }
    html += '</table>';
        
    
    // HTML表を表示
    document.write(html);
}