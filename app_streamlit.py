# Importando as bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

# Definindo a função principal
def main():
    
    # st.title('Data Viz')
    # st.subheader('Análise Exploratória de Dados')

    # Carregando a imagem de título e definindo o texto do header
    st.image('https://sc.movimentoods.org.br/wp-content/uploads/2019/10/qualirede.png', width=400)
    st.header('Um jeito simples de visualizar e analisar seus dados')
    st.sidebar.title('Data Viz')

    # Lendo o arquivo upado pelo usuário
    file = st.file_uploader('Escolha a base de dados CSV', type='csv')
    
    # Checando se o arquivo não está vazio
    if file is not None:
        
        # Inserindo os menus laterais
        st.sidebar.image('https://media.giphy.com/media/1klslCB8tbUmN4QoD4/giphy.gif', width=250)
        st.sidebar.header("Selecione:")
        # Checando quantas linhas do dataset o usuário quer ver
        columns = st.slider('Quantas linhas deseja ver?', min_value=1, max_value=50)
        
        # Lendo e exibindo o dataset
        st.markdown('**Seu arquivo**:')
        data = pd.read_csv(file)
        
        st.dataframe(data.head(columns))
        
        # Menu lateral para chegar o shape do dataset
        if st.sidebar.checkbox('Quero ver o shape dos meus dados'):
            st.markdown('**Quantidade de linhas:** ')
            st.markdown(data.shape[0])
            st.markdown('**Quantidade de colunas:**')
            st.markdown(data.shape[1])
                 
        #Menu lateral para chegar visualizar as colunas do dataset
        if st.sidebar.checkbox('Quero analisar as colunas'):
            all_columns = data.columns.tolist()
            selected_columns = st.multiselect('Selecione', all_columns)
            new_df = data[selected_columns].drop_duplicates(subset=None, keep='first')
            st.dataframe(new_df)
            
        #Menu lateral para contar o número de variáveis
        if st.sidebar.checkbox('Quero contas a quantidade de target/classes'):
            selected_plot = st.selectbox('Selecione o tipo de visualização', list(data.columns))
            st.markdown('**Contagem de Alvos/Classes**')
            st.write(data.iloc[:, data.columns.get_loc(selected_plot)].value_counts())
            
        #Menu lateral para ver os tipos de dados
        if st.sidebar.checkbox('Quero ver os tipos dos dados'):
            st.markdown('**Tipos de dados**')
            st.write(data.dtypes)
            
        #Menu lateral para ver a descrição dos dados
        if st.sidebar.checkbox('Quero a descrição dos meus dados'):
            st.markdown('**Descrição**')
            st.write(data.describe())
            
        #Menu lateral para selecionar o tipo de gráfico
        if st.sidebar.checkbox('Quero visualizar meus dados'):
            columns_names = data.columns.tolist()
            viz = ('line', 'bar', 'pie', 'hist', 'correlation', 'box')
            selected_plot = st.sidebar.selectbox('Selecione o tipo de visualização', viz)
            selected_columns_names = st.multiselect('Selecione as colunas', columns_names)
            
            # Gráfico de linha
            if selected_plot == 'line':
                custom_data = data[selected_columns_names]
                st.line_chart(custom_data)
              
            # Gráfico de barra
            elif selected_plot == 'bar':
                custom_data = data[selected_columns_names]
                st.bar_chart(custom_data)
                
            # Gráfico de pizza
            elif selected_plot == 'pie':
                st.write(data.iloc[:, -1].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()
                
            # Gráfico de correlação
            elif selected_plot == 'correlation':
                corr = data.corr()
                st.write(sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, 
                                                             annot=True))
                st.pyplot()
                
            # Outros gráficos
            else:
                custom_plot = data[selected_columns_names].plot(kind=selected_plot)
                st.pyplot()
            
        
        # Menu sobre mim
        #if st.sidebar.checkbox('Sobre'):
        html = """
        <br><br><br><br><br>
        <div>
        Desenvolvido pela equipe <a href="mailto:wilian.selzlein@qualirede.com.br">NGI</a>, 
        na <a href="https://www.qualirede.com.br/">Qualirede</a>.
        </div></b>
        """
        
        st.markdown(html,  unsafe_allow_html=True)
                                  
    
if __name__ == '__main__':
    main()

