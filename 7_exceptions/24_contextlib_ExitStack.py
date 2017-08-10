from contextlib import ExitStack


def merge_logs(output_path, *logs):
    with ExitStack() as stack:
        handles = [stack.enter_context(open(log)) for log in logs]
        output = open(output_path, 'wt')
        stack.enter_context(output)
        # I'm not sure that this example is correct
        from heapq import merge
        merge(output, handles)


