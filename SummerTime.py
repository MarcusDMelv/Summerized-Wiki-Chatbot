class SummerTime:
    # an algorithm that is able to summarize text
    # function lex_rank_analysis is created and defined
    def lex_rank_analysis (self, parser_configuration, number_of_lines_to_output, sumy=None):
        # Using LexRank
        # LexRank also incorporates an intelligent post-processing step which makes sure
        # that top sentences chosen for the summary are not too similar to each other.

        # import LexRankSummarizer from sumy api
        from sumy.summarizers.lex_rank import LexRankSummarizer
        # summarizer = the imported class LexRankSummarizer()
        summarizer = LexRankSummarizer()
        # Summarize the text and output n sentance
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        # debug raw output to console.
        print(f"\nBegin Raw summary from LexRank\n")
        for sentance in summarization_result:
            print(sentance)
        print(f"\nEnd Raw summary from LexRank\n")
        # Return summer Result
        return summarization_result

    # an algorithm able to summarize text
    # function lsa_analysis is created and defined
    def lsa_analysis(self, parser_configuration, number_of_lines_to_output):
        # using LSA
        # LSA works by projecting the data into a lower dimensional
        # space without any significant loss of information.
        # singular vectors can capture and represent word combination patterns which are recurring

        #import LsaSummarizer from sumy api
        from sumy.summarizers.lsa import LsaSummarizer
        # summarizer = the imported class LsaSummarizer()
        summarizer = LsaSummarizer()
        # Summarize the text and output n sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        # debug raw output to console.
        print(f"\nBegin Raw summary from LSA\n")
        for sentance in summarization_result:
            print(sentance)
        print(f"\nEnd Raw summary from LSA\n")
        # Return summer Result
        return summarization_result

    # an algorithm able to summarize text
    # function luhh_analysis is created and defined
    def luhn_analysis(self, parser_configuration, number_of_lines_to_output):
        # using Luhh
        # ranks sentences for summarization extracts by considering “significant” words,
        # which are frequently occurring words in a document
        from sumy.summarizers.luhn import LuhnSummarizer
        # summarizer = the imported class LuhnSummarizer()
        summarizer = LuhnSummarizer()
        # Summarize the text and output n sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        # debug raw output to console.
        print(f"\nBegin Raw summary from Luhn\n")
        for sentance in summarization_result:
            print(sentance)
        print(f"\nEnd Raw summary from Luhn\n")
        # Return summer Result
        return summarization_result

