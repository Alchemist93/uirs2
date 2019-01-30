function font_size_determination($block,height,width,font_size){
    $block.style.fontSize = fontSize + 'px';
    var block_height = $block.clientHeight;
    var block_width = $block.clientWidth;
    if (block_height > height || block_width > width){
        font_size = font_size*0.9;
        return font_size_determination($block,height,width,font_size);
    } else {
        return font_size;
    }
}

font_size_determination(document.querySelector('.left .frame .frame-content'), 500, 300, 25);
