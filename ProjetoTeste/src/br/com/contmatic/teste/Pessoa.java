package br.com.contmatic.teste;

public class Pessoa {

    private Integer idade;
    
    private String nome;

    public Integer getIdade() {
        return idade;
    }

    public void setIdade(Integer idade) {
        this.idade = idade;
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Pessoa [idade=" + idade + "]";
    }
    
}
