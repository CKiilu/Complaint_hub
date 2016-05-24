$(document).foundation();

function getProgram(path) {
    $('#id_department').change(function() {
        $.ajax({
            url: path,
            type: 'GET',
            data: {
                d_id: $('#id_department').val()
            },
            success: function(data) {
                $('#id_program').empty()
                $('#id_program').append($('<option>--------</option>'));
                for (var item in data) {
                    $('#id_program').append($('<option>' + data[item] + '</option>').val(item));
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
                $('#id_course').append($('<option>--------</option>'));
                for (var item in data) {
                    $('#id_course').append($('<option>' + data[item] + '</option>').val(item));
                }
            }
        });
    });
}