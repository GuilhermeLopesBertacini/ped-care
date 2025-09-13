# Requisitos Funcionais

1. **Cadastro de disponibilidade**

   * Permitir que o profissional da saúde cadastre seus horários disponíveis.
   * Definir horários diferentes por convênio.

2. **Agendamento de consultas**

   * O paciente deve conseguir marcar consultas em horários livres.
   * O chatbot deve confirmar o agendamento automaticamente.

3. **Reagendamento e cancelamento**

   * Possibilidade de reagendar consultas respeitando as regras do profissional.
   * Cancelamentos feitos pelo paciente devem atualizar automaticamente a agenda do profissional.

4. **Lista de priorização**

   * Permitir que pacientes em situação de prioridade (ex.: urgência, retorno de acompanhamento) sejam atendidos com preferência.

5. **Integração com convênios**

   * Considerar os convênios aceitos pelo profissional.
   * Exibir apenas horários disponíveis para determinado convênio.

6. **Integração com canais de atendimento**

   * Atendimento via **WhatsApp (WhatsApp Business API)**.
   * Atendimento via **API para integração em landing page** do médico.

7. **Integração com sistemas de agenda existentes**

   * Sincronização bidirecional com sistemas externos de gestão de agenda já utilizados pelo profissional.

8. **Mensagens automáticas**

   * Enviar mensagens de confirmação, lembretes e cancelamento.
   * Personalização de mensagens conforme regras do profissional.

9. **Dashboard para profissionais**

   * Visualizar agenda em tempo real.
   * Consultar métricas de desempenho:

     * Horários mais requisitados.
     * Taxa de cancelamento de consultas.
     * Tempo médio de espera para agendamento.
     * Distribuição de agendamentos por convênio.

10. **Histórico de interações**

    * Registrar atendimentos e interações do chatbot com pacientes.


# Requisitos Não Funcionais

1. **Disponibilidade**

   * O sistema deve estar disponível 24/7, garantindo que pacientes possam agendar a qualquer momento.

2. **Escalabilidade**

   * Capacidade de suportar múltiplos profissionais e clínicas simultaneamente.

3. **Segurança**

   * Proteção de dados sensíveis conforme **LGPD** (Lei Geral de Proteção de Dados).
   * Autenticação segura para profissionais.

4. **Desempenho**

   * O tempo de resposta do chatbot deve ser inferior a **2 segundos** em 95% das interações.

5. **Integração**

   * APIs RESTful documentadas e padronizadas.
   * Suporte a integração com calendários externos (Google Calendar, Outlook, sistemas médicos).

6. **Usabilidade**

   * Conversas intuitivas e humanizadas no chatbot.
   * Interface de dashboard responsiva e acessível.

7. **Manutenibilidade**

   * Código estruturado com **DDD (Domain-Driven Design)**.
   * Camadas separadas (Controller, Business, Model).

8. **Confiabilidade**

   * Registro de logs e monitoramento de falhas.
   * Backup automático da base de dados.

9. **Portabilidade**

   * Hospedagem em nuvem (compatível com AWS, Azure ou GCP).
   * Suporte a diferentes navegadores e dispositivos móveis.

10. **Testabilidade**

    * Desenvolvimento orientado a testes (TDD/BDD).
    * Automação de testes unitários, integração e aceitação.

