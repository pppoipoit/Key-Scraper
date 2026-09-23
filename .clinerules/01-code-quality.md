# Code Quality

- ทำตาม style, convention และ architecture ที่มีอยู่ใน repository ก่อน
- ใช้ชื่อที่สื่อความหมาย หลีกเลี่ยง magic values และ code ซ้ำโดยไม่จำเป็น
- แยก logic ที่ซับซ้อนให้ test ได้
- รักษา error handling, loading state, empty state และ validation ตามความเหมาะสม
- อย่าสร้าง abstraction เกินจำเป็น
- อย่า refactor เพื่อความสวยอย่างเดียว หากไม่อยู่ใน scope
- ทุก change ต้องมีเหตุผลที่โยงกับ acceptance criteria
- ถ้าพบ code smell สำคัญ ให้รายงานและเพิ่ม backlog แทนการแก้เองนอก scope
- ห้ามปิด type checking, lint rules หรือ test เพื่อให้ build ผ่าน โดยไม่ขออนุมัติ