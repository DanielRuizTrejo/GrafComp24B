from manim import *

class VectorAnalysis(Scene):
    def construct(self):
        
        title = Text("Análisis de Vectores: Producto Punto y Ortogonalidad").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        #Formula producto punto
        formula_text = MathTex(r"\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2").scale(1.2).to_edge(DOWN)
        self.play(Write(formula_text))
        self.wait(1)

        #Prier ejeplo
        vector_a1 = Vector([4, -1], color=BLUE).scale(0.5)  # Reducir tamaño
        vector_b1 = Vector([2, 8], color=RED).scale(0.5)   # Reducir tamaño
        label_a1 = MathTex(r"\vec{a} = 4\hat{i} - \hat{j}").scale(0.8).next_to(vector_a1, DOWN)
        label_b1 = MathTex(r"\vec{b} = 2\hat{i} + 8\hat{j}").scale(0.8).next_to(vector_b1, DOWN)

        #Centrar el vector
        vector_a1.shift(LEFT * 2)  
        vector_b1.shift(RIGHT * 2) 

        #crea los vectores
        self.play(Create(vector_a1), Write(label_a1))
        self.play(Create(vector_b1), Write(label_b1))
        self.wait(1)

    
        dot_product_1 = 4 * 2 + (-1) * 8  
        result_text_1 = Text("Ortogonal (Producto Punto = 0)").scale(0.8).next_to(formula_text, DOWN)
        self.play(Write(result_text_1))

        #Pausa
        self.wait(2)
        self.play(FadeOut(vector_a1, vector_b1, label_a1, label_b1, result_text_1))

        
        vector_a2 = Vector([6, -18], color=BLUE).scale(0.5)  
        vector_b2 = Vector([-4, 12], color=RED).scale(0.5)   
        label_a2 = MathTex(r"\vec{a} = 6\hat{i} - 18\hat{j}").scale(0.8).next_to(vector_a2, DOWN)
        label_b2 = MathTex(r"\vec{b} = -4\hat{i} + 12\hat{j}").scale(0.8).next_to(vector_b2, DOWN)

        
        vector_a2.shift(LEFT * 2)  
        vector_b2.shift(RIGHT * 2)  

        
        self.play(Create(vector_a2), Write(label_a2))
        self.play(Create(vector_b2), Write(label_b2))
        self.wait(1)

        dot_product_2 = 6 * -4 + (-18) * 12  
        result_text_2 = Text("No Ortogonal (Producto Punto ≠ 0)").scale(0.8).next_to(formula_text, DOWN)
        self.play(Write(result_text_2))

        self.wait(2)

        self.play(FadeOut(vector_a2, vector_b2, label_a2, label_b2, result_text_2, formula_text, title))
