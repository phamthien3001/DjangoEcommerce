$(document).ready(function (){

    $('.increment-btn').click(function (e) {
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        // var value = parseInt(inc_value, 100);
        // value = isNaN(value) ? 0 : value;
        // console.log(value)
        if(inc_value < 100){
            inc_value++;
            $(this).closest('.product_data').find('.qty-input').val(inc_value);
        }
     });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        if(dec_value > 1){
            dec_value--;
            $(this).closest('.product_data').find('.qty-input').val(dec_value);
        }
     });
});