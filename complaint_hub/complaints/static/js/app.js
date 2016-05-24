$(document).foundation();

function getProgram(path) {
    $('#id_program').change(function() {
        $.ajax({
            url: path,
            type: 'GET',
            data: {
                p_id: $('#id_program').val()
            },
            success: function(data) {
                $('#id_course').empty()
                for (var item in data) {
                    $('#id_course').append($('<option>' + data[item] + '</option>').val(item));
                }
            }
        });
    });
}

function getCourses(path) {
    $('#id_program').change(function() {
        $.ajax({
            url: path,
            type: 'GET',
            data: {
                p_id: $('#id_program').val()
            },
            success: function(data) {
                $('#id_course').empty()
                for (var item in data) {
                    $('#id_course').append($('<option>' + data[item] + '</option>').val(item));
                }
            }
        });
    });
}