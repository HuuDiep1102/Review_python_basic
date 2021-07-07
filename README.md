So sánh thời gian thực thi giữa thread và process 
Theo em tìm hiểu thì tác vụ trong trường hợp này của mình là dạng
IO- bound ( tác vụ phần lớn thời gian để chờ đợi kết quả từ hệ thống khác như network - cụ thể ở đây là phản hồi từ các trang web trong danh sách, database, ...) khác với kiểu CPU-bound ( tác vụ dành phần lớn thời gian để tính toán trong CPU). Với các tác vụ IO- bound thì multithread sẽ mang lại hiệu năng tốt hơn nhưng lại có thể gây suy giảm hiệu năng với các tác vụ CPU-bound mà nguyên nhân là do cơ chế Global Interpreter Lock (GIL) chỉ cho phép 1 thread thực thi tại một thời điểm. Do GIL không ảnh hưởng nhiều với tác vụ IO-bound do 1 thread chỉ thực hiện các request và đợi kết quả phản hồi nên trong thời gian chờ đợi thread khác sẽ được chuyển vào thực hiện các request, nhờ đó mà tối ưu được thời gian chờ đợi, dẫn đến tăng hiệu năng. 

Kết luận là Multithread sẽ mang lại hiệu năng tốt hơn từ đó dẫn đến thời gian thực thi ngắn hơn.

P/S: Nhưng do môi trường thực tế em có chạy 2 cách này thì chưa thể kết luận bằng thực nghiệm cái nào chạy nhanh hơn. Em mong anh giải đáp thắc mắc này cho em ạ. Em cảm ơn

