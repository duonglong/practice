public enum Language
{
    English, German, Spanish
}

public class SpeakerFactory
{
    public static ISpeaker CreateSpeaker(Language language)
    {
        switch (language)
        {
            case Language.English:
                return new EnglishSpeaker();
            case Language.German:
                return new GermanSpeaker();
            case Language.Spanish:
                return new SpanishSpeaker();
            default:
                throw new ApplicationException("No speaker can speak such language");
        }
    }
}

[STAThread]
static void Main()
{
    //This is your client code.
    ISpeaker speaker = SpeakerFactory.CreateSpeaker(Language.English);
    speaker.Speak();
    Console.ReadLine();
}

public interface ISpeaker
{
    void Speak();
}

public class EnglishSpeaker : ISpeaker
{
    public EnglishSpeaker() { }

    #region ISpeaker Members

    public void Speak()
    {
        Console.WriteLine("I speak English.");
    }

    #endregion
}

public class GermanSpeaker : ISpeaker
{
    public GermanSpeaker() { }

    #region ISpeaker Members

    public void Speak()
    {
        Console.WriteLine("I speak German.");
    }

    #endregion
}

public class SpanishSpeaker : ISpeaker
{
    public SpanishSpeaker() { }

    #region ISpeaker Members

    public void Speak()
    {
        Console.WriteLine("I speak Spanish.");
    }

    #endregion
}