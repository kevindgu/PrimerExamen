"""Generador infinito de preguntas sin repetir."""
import random


class InfiniteGenerator:
    def __init__(self, generator_fn, topics, dificultad="Normal"):
        self.generator_fn = generator_fn
        self.topics = list(topics)
        self.dificultad = dificultad
        self.used_ids = set()
        self.fail_count = 0  # cuántas veces seguidas no pudo generar nueva

    def _make_id(self, q):
        """Crea ID único de la pregunta basado en su contenido."""
        # Usamos question text + answer como ID
        return hash((q.get('question', ''), str(q.get('answer', ''))))

    def next(self):
        """Genera siguiente pregunta que no se haya usado."""
        max_attempts = 50
        for _ in range(max_attempts):
            topic = random.choice(self.topics)
            q = self.generator_fn(topic, self.dificultad)
            qid = self._make_id(q)
            if qid not in self.used_ids:
                self.used_ids.add(qid)
                q['_qid'] = qid
                self.fail_count = 0
                return q
        # Si después de 50 intentos no encuentra nueva, resetea el pool
        self.used_ids.clear()
        self.fail_count += 1
        q = self.generator_fn(random.choice(self.topics), self.dificultad)
        qid = self._make_id(q)
        self.used_ids.add(qid)
        q['_qid'] = qid
        return q

    @property
    def questions_seen(self):
        return len(self.used_ids)
