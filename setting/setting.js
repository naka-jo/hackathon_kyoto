const belong_list = document.getElementById('belong_list');
const colCount = document.querySelectorAll('#belong_list');

function add() {
    belong_list.insertAdjacentHTML('beforeend',
    `<tr>${'<td><input></td>'.repeat(colCount)}</tr>`);
}

function del() {
    if(belong_list.rows.length > 1) {
    belong_list.deleteRow(belong_list.rows.length - 1);
    }
}