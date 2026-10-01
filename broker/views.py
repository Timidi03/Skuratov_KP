from django.shortcuts import render

def index(request):
  limit = int(request.GET.get('limit', 10))
  data = {
    'admin': 3,
    'ivan': 12,
    'olga': 7,
    'root': 25
  }
  rows = [(u, n, 'block' if n > limit else 'ok') for u, n in data.items()]
  blocked = sum(1 for r in rows if r[2] == 'block')
  return render(
    request,
    "broker/index.html",
    {
      'limit': limit,
      'rows': rows,
      'names': list(data),
      'counts': list(data.values()),
      'blocked': blocked,
      'ok': len(rows) - blocked
    }
  )
