from graphviz import Digraph

# Khởi tạo đồ thị tư duy
mind_map = Digraph('Thuyết Đa Trí Tuệ', filename='da_tri_tue_mind_map', format='png')
mind_map.attr(rankdir='TB', size='10,10')

# Thêm nút trung tâm
mind_map.node('TT', 'Thuyết Đa Trí Tuệ', shape='ellipse', style='filled', color='lightblue')

# Thêm các nhánh chính
categories = {
    'Logic - Toán học': 'Khả năng phân tích, tư duy logic, giải quyết vấn đề, sử dụng số liệu.',
    'Ngôn ngữ': 'Khả năng sử dụng ngôn ngữ nói và viết, diễn đạt và hiểu từ ngữ.',
    'Tương tác': 'Khả năng giao tiếp, hiểu biết tâm lý và cảm xúc của người khác.',
    'Âm nhạc': 'Khả năng cảm nhận âm thanh, giai điệu, nhịp điệu và sáng tác âm nhạc.',
    'Không gian': 'Khả năng tưởng tượng, hình dung không gian, thiết kế, sáng tạo.',
    'Thiên nhiên': 'Khả năng nhận thức và cảm nhận về môi trường tự nhiên, yêu thiên nhiên.',
    'Vận động': 'Khả năng điều khiển và vận dụng các chuyển động cơ thể.',
    'Nội tâm': 'Khả năng tự nhận thức, hiểu rõ bản thân, khám phá cảm xúc.'
}

for key, desc in categories.items():
    mind_map.node(key, f'{key}\\n{desc}', shape='box', style='filled', color='lightgreen')
    mind_map.edge('TT', key)

# Lưu và xuất sơ đồ tư duy
mind_map.render(view=True)
