
#google-api #documentation
#comofazer 
> This application leads you to handle google-sheets-doc. Displaying data using streamlit. It consumes Google-Drive-Api and Google-Sheets-Api as an integration to fetch data.


> Esta Pagina cobre o básico de como criar uma planilha no **Google** usando **GOOGLE API SERVICE** e a **API do Google**

# 1 Set up Google console

Primeiro precisamos criar uma conta no Google console, fazendo Login com nossa conta de usuário
[Google-Cloud](https://accounts.google.com/v3/signin/confirmidentifier?authuser=0&continue=https%3A%2F%2Fconsole.cloud.google.com%2F&dsh=S-1626032937%3A1763127272813261&followup=https%3A%2F%2Fconsole.cloud.google.com%2F&ifkv=ARESoU1S_BORiWkl12lRwErJx72pjWlpw9Eac-5tZv0IGMJBM0wB-tpx8FEDcg9npsnXKx4QOc2RBg&osid=1&passive=1209600&service=cloudconsole&flowName=GlifWebSignIn&flowEntry=ServiceLogin)

Depois de realizar o Login e criar suas credenciais, salve o arquivo de senha dentro do projeto de Python;
Você pode ver algum vídeo de referencia, não irei me aprofundar, pois a integração é simples.


---
# 2 Pastas e Projeto
Após realizar as configurações do passo anterior, crie uma pasta e um arquivo **Google Sheets** com algum dado dentro da sua conta do **Google Drive**.

Realizado esta configuração, retorne a conta de serviço que criou no passo anterior e copie o **Email** que foi gerado
>Você deve compartilhar a pasta e o arquivo **Google Sheets** com o Email que foi gerado, dando permissão de **editor** para ele.


---
# 3 Instalando dependências

As dependências do projeto e o setup inicial estão na documentação oficial do Google.
> [Documentação oficial](https://developers.google.com/workspace/sheets/api/quickstart/python?hl=pt-br)
> Você pode conferir tudo por la.

Os pacotes necessários são os seguintes:
```
pip install --upgrade pandas gspread oauth2client dotenv
```


---
# 4 Configurando as Variáveis de ambiente

Agora que temos as dependências instaladas e também permitimos que o **Google** gerencie nossa planilha e a pasta em que a planilha esta, precisamos do ID da planilha, que será usada no código dentro do arquivo **.env**

Você ira encontrar o **ID da planilha** dentro da **URL**:

> [!ID da planilha] ID
> https: // docs.google.com/spreadsheets/d/ O código até a ou barra /


### Dentro do Projeto:
Agora dentro do projeto, crie um arquivo **.env** no seguinte formato:

```
PLANILHA_ID=1ibEzVIf5REWPXurPV3qzZO2p-bFP32KZh3EwcPj3-AA
FILENAME=client_data.**json**
```
Onde o **PLANILHA_ID** será o ID copiado da URL
E o **FILENAME** será o o nome do arquivo de senha baixado da **Conta de serviço**

> Importante: Ambos arquivos devem ser mantidos em segredo, pois permitem acesso a suas informações pessoais.



---


# 1 Set up Google Console

First, we need to create an account in Google Console by logging in with our user account:  
Google-Cloud: (login link)

After logging in and creating your credentials, save the password file inside your Python project.  
You may watch some reference video tutorials — I won't go deep here since the integration is simple.

---

# 2 Folders and Project

After completing the previous setup step, create a folder and a **Google Sheets** file with some data inside your **Google Drive** account.

After doing this, go back to the service account you created in the previous step and copy the **Email** generated for it.  
> You must share the folder and the **Google Sheets** file with that Email, granting **editor** permission.

---

# 3 Installing Dependencies

The project dependencies and initial setup are covered in Google’s official documentation.  
> [Official documentation](https://developers.google.com/workspace/sheets/api/quickstart/python?hl=pt-br)

The required packages are:


```
pip install --upgrade pandas gspread oauth2client dotenv
```


---
# 4 Setting Up Environment Variables

Now that we have installed the dependencies and allowed **Google** to manage our spreadsheet and the folder it is in, we need the spreadsheet ID, which will be used in the `.env` file.

You will find the **Spreadsheet ID** in the **URL**:

> https://docs.google.com/spreadsheets/d/ THE-CODE-UNTIL-THE-NEXT-SLASH /

### Inside the Project:

Inside your project, create a `.env` file with the following format:

```

PLANILHA_ID=1ibEzVIf5REWPXurPV3qzZO2p-bFP32KZh3EwcPj3-AA  
FILENAME=client_data.json

```

Where **PLANILHA_ID** is the ID copied from the URL,  
and **FILENAME** is the name of the credentials (password) file downloaded from the **Service Account**.

> Important: Both files must be kept secret, as they allow access to your personal information.
